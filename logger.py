from models.log import Log

def create_log(db, user_id, action, table_name, record_id):
    log = Log(
        user_id=user_id,
        action=action,
        table_name=table_name,
        record_id =record_id
    )

    db.add(log)
