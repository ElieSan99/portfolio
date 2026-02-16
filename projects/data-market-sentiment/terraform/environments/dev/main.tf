terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

module "iam" {
  source     = "../../modules/iam"
  project_id = var.project_id
  env        = var.env
}

module "gcs" {
  source      = "../../modules/gcs"
  bucket_name = "${var.project_id}-reddit-analytics"
  region      = var.region
  env         = var.env
}

module "bigquery" {
  source      = "../../modules/bigquery"
  region      = var.region
  env         = var.env
  bucket_name = module.gcs.bucket_name
}

module "composer" {
  source                = "../../modules/composer"
  project_id            = var.project_id
  region                = var.region
  env                   = var.env
  service_account_email = module.iam.airflow_sa_email
  airflow_sa_iam_bindings = module.iam.airflow_sa_iam_bindings

  depends_on = [module.iam]
}
