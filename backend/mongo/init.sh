#!/bin/bash

collections=("professions" "users" "skills" "cvs" "vacancies" "chat_messages" "chats" "matches" "notes")

for collection in "${collections[@]}"
do
    echo "Importing $collection..."
    mongoimport --host $db_host --db unknown_mongo_development --collection "$collection" --file "seed/$collection.json" --jsonArray --mode upsert -u root -p example --authenticationDatabase=admin

    if [ $? -eq 0 ]; then
        echo "Successfully imported $collection"
    else
        echo "Failed to import $collection"
    fi
done