Perfect! Since you’d like to use **Docker** to set up Prometheus, Node Exporter, and Grafana, I’ll walk you through each step to get everything running **locally using Docker**.

---

## ✅ **Step-by-Step Setup using Docker**

### **📁 Step 1: Create a Project Directory**
Open a terminal and create a new folder for your project:
```bash
mkdir prometheus-grafana-monitoring
cd prometheus-grafana-monitoring
```

---

### **📝 Step 2: Create the `docker-compose.yml`**
Create a file named `docker-compose.yml`:
```bash
touch docker-compose.yml
```

Paste this into it:
```yaml
version: '3'

services:
  prometheus:
    image: prom/prometheus
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3000:3000"
    depends_on:
      - prometheus

  node-exporter:
    image: prom/node-exporter
    container_name: node-exporter
    ports:
      - "9100:9100"
```

---

### **🛠️ Step 3: Create `prometheus.yml` Configuration**
In the same directory, create a file:
```bash
touch prometheus.yml
```

Paste this:
```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
```

---

### **🚀 Step 4: Launch the Stack**
Run the services using Docker Compose:
```bash
docker-compose up -d
```

---

### **🌐 Step 5: Verify Everything is Running**

- **Prometheus:** http://localhost:9090  
  Go to **Status > Targets** → `node-exporter` should show **UP**.

- **Grafana:** http://localhost:3000  
  Login with default:  
  - **Username:** `admin`  
  - **Password:** `admin`

---

### **📊 Step 6: Set Up Grafana Dashboard**

1. Go to **Configuration → Data Sources → Add data source**
2. Choose **Prometheus**
3. Set the URL to:
   ```
   http://prometheus:9090
   ```
4. Click **Save & Test**

Now:

1. Click **+ Create → Import**
2. Enter Dashboard ID: `1860`
3. Select the Prometheus data source and click **Import**

You'll now see CPU, memory, and other system metrics!

---

