from version2.app import app, BASE_DIR, PROJECT_DIR


if __name__ == "__main__":
    app.run(debug=True)
    print(PROJECT_DIR)
