# Usage

To use log_analyzer in a project:

```python
import log_analyzer
```

### with the default configuration
```bash
log_analyzer
```

## Example configuration file (config.toml):
```bash
REPORT_SIZE = 10
REPORT_DIR = "./reports"
TEMPLATE_PATH = "./templates/report.html"
LOG_DIR = "./logs"
LOG_PATTERN = 'nginx_access_ui\.log_(\d{8})-\d{6}-[a-f0-9]+(?:\.gz)?$'
```

### with a config when launching from the console
```bash
log_analyzer --config /путь/к/config.toml
```
