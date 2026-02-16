resource "google_storage_bucket" "reddit_analytics" {
  name          = var.bucket_name
  location      = var.region
  force_destroy = true

  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 90
    }
    action {
      type          = "SetStorageClass"
      storage_class = "NEARLINE"
    }
  }

  lifecycle_rule {
    condition {
      age = 365
    }
    action {
      type          = "SetStorageClass"
      storage_class = "COLDLINE"
    }
  }

  lifecycle_rule {
    condition {
      age = 730
    }
    action {
      type = "Delete"
    }
  }

  labels = {
    env  = var.env
    part = "ingestion"
  }
}

# Dossiers (préfixes) simulés via des objets vides 
# Note : GCS n'a pas de vrais dossiers, mais c'est utile pour la clarté
resource "google_storage_bucket_object" "bronze_folder" {
  name    = "bronze/"
  content = " "
  bucket  = google_storage_bucket.reddit_analytics.name
}

resource "google_storage_bucket_object" "ml_artifacts_folder" {
  name    = "ml_artifacts/"
  content = " "
  bucket  = google_storage_bucket.reddit_analytics.name
}

resource "google_storage_bucket_object" "airflow_temp_folder" {
  name    = "airflow_temp/"
  content = " "
  bucket  = google_storage_bucket.reddit_analytics.name
}
