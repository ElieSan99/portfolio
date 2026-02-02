output "kubernetes_cluster_name" {
  value = google_container_cluster.primary.name
}

output "kubernetes_cluster_endpoint" {
  value = google_container_cluster.primary.endpoint
}

output "sql_instance_connection_name" {
  value = google_sql_database_instance.instance.connection_name
}

output "vertex_ai_index_id" {
  value = google_vertex_ai_index.market_states_index.id
}

output "vertex_ai_endpoint_id" {
  value = google_vertex_ai_index_endpoint.index_endpoint.id
}

output "storage_bucket_url" {
  value = google_storage_bucket.rl_checkpoints.url
}

output "secret_name" {
  value = google_secret_manager_secret.broker_keys.name
}
