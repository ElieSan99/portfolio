resource "google_composer_environment" "reddit_env" {
  name    = "${var.environment_name}-${var.env}"
  region  = var.region
  project = var.project_id

  # Forcer la dépendance sur les droits IAM
  depends_on = [
    var.airflow_sa_iam_bindings
  ]

  config {
    # Structure Cloud Composer 3
    # Note: node_count et nodes_config sont plus simples
    
    software_config {
      image_version = var.airflow_image_version
      
      pypi_packages = {
        # Je réactive les packages essentiels car CP3 est plus résilient au boot
        praw                            = ">=7.7.0"
        google-cloud-bigquery           = ">=3.11.0"
        google-cloud-storage            = ">=2.10.0"
        pandas                          = ">=2.0.0"
        pyarrow                         = ">=14.0.0"
        great-expectations              = ">=0.18.0"
      }

      env_variables = {
        ENV = var.env
      }
    }

    node_config {
      service_account = var.service_account_email
    }

    # Configuration des ressources simplifiée dans Composer 3
    # Utilisation du bloc standard pour Small environment
  }

  timeouts {
    create = "60m"
    update = "60m"
  }
}