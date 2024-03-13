from app.database import get_db

def result_formatter(results):
  out = []
  for result in results:
    res = {
      "id": result[0],
      "name": result[1],
      "summary": result[2],
      "description": result[3],
      "id_done": result[4]
    }
    out.append(res)
  return out

def scan():
  conn = get_db()
  cursor = conn.execute("SELECT * FROM task")
  results = cursor.fetchall()
  cursor.close()
  return result_formatter(results)

def select_by_id(task_id):
  conn = get_db()
  cursor = conn.execute("SELECT * FROM task WHERE id = ?", (task_id,))
  # fetchall returns a list of tuples, so we need to extract the first element of the list
  result = cursor.fetchall()
  cursor.close()
  if result:
    return result_formatter([result])[0]
  return {}

def insert(task_data):
  data_tuple = (
    task_data.get("name"),
    task_data.get("summary"),
    task_data.get("description")
  )

  statement = """
    INSERT INTO task (
      name, summary, description
    ) VALUES (?, ?, ?)
    """
  conn = get_db()
  conn.execute(statement, data_tuple)
  conn.commit()

def update_by_id(task_id, task_data):
  data_tuple = (
    task_data.get("name"),
    task_data.get("summary"),
    task_data.get("description"),
    task_data.get("id_done"),
    task_id
  )

  statement = """
    UPDATE task
    SET
      name = ?,
      summary = ?,
      description = ?
      is_done = ?
    WHERE id = ?
    """
  conn = get_db()
  conn.execute(statement, data_tuple)
  conn.commit()

def delete(task_id):
  conn = get_db()
  conn.execute("DELETE FROM task WHERE id = ?", (task_id,))
  conn.commit()