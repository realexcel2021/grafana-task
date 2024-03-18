# Grafana Dashboard for VMs Monitoring

We deployed Prometheus and cAdvisor containers using Docker Compose. Within the Prometheus stack, we utilized the `--enable-feature=agent` flag to enable specific features and configured it to forward metrics to `metrics.onemedtest.com`. Both the scrape interval and scrape configurations were set up in prometheus.yml. To verify that `onemedtest.com` was successfully receiving the metrics, we included the` safe_mac_node` identifier for easy tracking. Additionally, we integrated the `remote-write` capability in the configuration of `onemedtest.com` to facilitate this process.

See Grafana charts for CPU and Memory usage

![Alt text](<Screen Shot 2024-03-18 at 15.50.56.png>)

![Alt text](<Screen Shot 2024-03-18 at 15.52.33.png>)