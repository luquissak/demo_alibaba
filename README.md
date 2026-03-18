# demo_alibaba
Teste de Modelos e Apps Alibaba Qwen

# Create venv

```bash
py -m venv .venv
.venv\scripts\activate
.venv\scripts\python -m pip install --upgrade pip
.venv\scripts\activate && .venv\Scripts\pip install -r requirements.txt
```

# Load var
```bash
get-content .env | foreach {
    $name, $value = $_.split('=')
    set-content env:\$name $value
    echo $name $value
}
```

# Run

```bash
.venv\scripts\activate && .venv\Scripts\python src\demo_qwen.py
```