CURR_PATH=$(cd $(dirname $0);pwd)
psql -U pgadmin -d fund -f $CURR_PATH/*.sql
