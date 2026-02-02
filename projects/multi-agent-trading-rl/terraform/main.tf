provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

# 1. GKE Autopilot Cluster
resource "google_container_cluster" "primary" {
  name     = var.cluster_name
  location = var.region

  enable_autopilot = true

  # Set network and subnetwork if needed, otherwise uses default
  # network    = "default"
  # subnetwork = "default"

  ip_allocation_policy {
    cluster_ipv4_cidr_block  = ""
    services_ipv4_cidr_block = ""
  }
}

# 2. Cloud SQL (PostgreSQL)
resource "google_sql_database_instance" "instance" {
  name             = var.db_instance_name
  region           = var.region
  database_version = "POSTGRES_14"

  settings {
    tier = "db-f1-micro" # Smallest tier for cost efficiency
  }

  deletion_protection = false # Set to true for production
}

resource "google_sql_database" "database" {
  name     = "trading_data"
  instance = google_sql_database_instance.instance.name
}

# 3. Vertex AI Vector Search (Index & Endpoint)
resource "google_vertex_ai_index" "market_states_index" {
  display_name = "market-states-index"
  description  = "Index for storing market state embeddings"
  metadata {
    contents_delta_uri = "gs://${var.bucket_name}/index_metadata"
    config {
      dimensions                  = 1536
      approximate_neighbors_count = 150
      distance_measure_type       = "COSINE"
      algorithm_config {
        brute_force_config {}
      }
    }
  }
  index_update_method = "STREAM_UPDATE"
}

resource "google_vertex_ai_index_endpoint" "index_endpoint" {
  display_name = "market-states-endpoint"
  description  = "Endpoint for querying market states"
  region       = var.region
}

# 4. Secret Manager for API Keys
resource "google_secret_manager_secret" "broker_keys" {
  secret_id = var.secret_id

  replication {
    automatic = true
  }
}

# 5. Cloud Storage for RL Checkpoints
resource "google_storage_bucket" "rl_checkpoints" {
  name     = var.bucket_name
  location = var.region
  force_destroy = true

  uniform_bucket_level_access = true
}
