mkdir -p ~/.streamlit/
echo "[general]
email = \"ntscheumann@gmail.comcom\"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml