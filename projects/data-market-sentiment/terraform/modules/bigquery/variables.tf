variable "region" {
  type        = string
  description = "Région GCP"
}

variable "env" {
  type        = string
  description = "Environnement (dev, prod)"
}

variable "bucket_name" {
  type        = string
  description = "Nom du bucket GCS pour les tables externes"
}
