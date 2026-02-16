variable "project_id" {
  type        = string
  description = "ID du projet GCP"
}

variable "region" {
  type        = string
  description = "Région GCP"
}

variable "env" {
  type        = string
  description = "Environnement (dev, prod)"
}

variable "service_account_email" {
  type        = string
  description = "Email du compte de service pour Composer"
}

variable "environment_name" {
  type        = string
  description = "Nom de l'environnement Composer"
  default     = "composer-reddit-analytics"
}

variable "airflow_image_version" {
  type        = string
  description = "Version de l'image Airflow/Composer"
  default     = "composer-3-airflow-2.10.2" # Passage en Composer 3
}

variable "airflow_sa_iam_bindings" {
  type        = any
  description = "Bindings IAM pour forcer la dépendance"
  default     = []
}
