output "airflow_sa_email" {
  value = google_service_account.airflow_sa.email
}

output "airflow_sa_iam_bindings" {
  value = [
    google_project_iam_member.gcs_admin.id,
    google_project_iam_member.bq_editor.id,
    google_project_iam_member.bq_job_user.id,
    google_project_iam_member.composer_worker.id,
    google_project_iam_member.logging_writer.id,
    google_project_iam_member.monitoring_writer.id,
    google_project_iam_member.artifact_registry_reader.id,
    google_project_iam_member.composer_agent_v2_ext.id,
    google_service_account_iam_member.composer_agent_sa_user.id,
    google_project_iam_member.composer_agent_sa_user_project.id
  ]
}
