resource "google_bigquery_dataset" "bronze" {
  dataset_id                  = "bronze_reddit"
  friendly_name               = "Bronze Layer - Raw Reddit Data"
  description                 = "Données brutes Reddit ingérées depuis GCS au format Parquet"
  location                    = var.region
  default_table_expiration_ms = null

  labels = {
    env   = var.env
    layer = "bronze"
  }
}

resource "google_bigquery_dataset" "silver" {
  dataset_id                  = "silver_reddit"
  friendly_name               = "Silver Layer - Cleaned Reddit Data"
  description                 = "Données Reddit nettoyées et transformées"
  location                    = var.region
  default_table_expiration_ms = null

  labels = {
    env   = var.env
    layer = "silver"
  }
}

resource "google_bigquery_dataset" "gold" {
  dataset_id                  = "gold_reddit"
  friendly_name               = "Gold Layer - Analytical Reddit Data"
  description                 = "Données prêtes pour l'analyse et le ML"
  location                    = var.region
  default_table_expiration_ms = null

  labels = {
    env   = var.env
    layer = "gold"
  }
}

# Table externe Bronze pointant vers GCS
# On utilise le partitionnement Hive
# Note : La table externe peut échouer au premier apply si le bucket est vide.
# Il est recommandé de la déployer APRÈS une première ingestion Airflow
# ou de commenter cette ressource pour le premier 'terraform apply'.
# resource "google_bigquery_table" "external_reddit_posts" {
#   dataset_id = google_bigquery_dataset.bronze.dataset_id
#   table_id   = "reddit_posts_ext"
# 
#   external_data_configuration {
#     autodetect    = true
#     source_format = "PARQUET"
#     source_uris   = ["gs://${var.bucket_name}/bronze/posts/*"]
# 
#     hive_partitioning_options {
#       mode                   = "AUTO"
#       source_uri_prefix      = "gs://${var.bucket_name}/bronze/posts"
#       require_partition_filter = false
#     }
#   }
# 
#   deletion_protection = false
# }
