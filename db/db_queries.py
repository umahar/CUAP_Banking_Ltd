"""manages all db queries"""

from db.db_connection import create_connection


def get_bill_id(bill_id):
    """Fetches a bill by its id."""
    conn = create_connection()
    try:
        cursor = conn.cursor()
        sql = "SELECT bill_id FROM bills WHERE bill_id=%s;"
        cursor.execute(sql, (bill_id,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Error getting bill id: {e}")
        return None
    finally:
        cursor.close()
        conn.close()
