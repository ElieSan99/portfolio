variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "europe-west1"
}

variable "zone" {
  description = "The GCP zone"
  type        = string
  default     = "europe-west1-b"
}

variable "cluster_name" {
  description = "The name of the GKE Autopilot cluster"
  type        = string
  default     = "trading-agents-cluster"
}

variable "db_instance_name" {
  description = "The name of the Cloud SQL instance"
  type        = string
  default     = "trading-db-instance"
}

variable "bucket_name" {
  description = "The name of the Cloud Storage bucket for RL checkpoints"
  type        = string
}

variable "secret_id" {
  description = "The ID of the secret in Secret Manager"
  type        = string
  default     = "broker-api-keys"
}
