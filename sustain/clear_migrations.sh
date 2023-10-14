#!/bin/bash

# Loop through each Django app's migration folder
for app in challenges feed friends map profiles sustain users # Replace with your actual app names
do
  echo "Removing migrations in $app"
  find ./$app/migrations/ -type f -not -name '__init__.py' -delete
  find ./$app/migrations/__pycache__/ -type f -delete
  find ./$app/__pycache__/ -type f -delete
done

# Remove the SQLite database
echo "Removing SQLite database"
rm db.sqlite3  # Replace with your actual database name if different

# Done
echo "Cleanup complete."
