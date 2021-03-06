




from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()

# utilizar tipos de datos más complejos.
# UUID
# datetime.datetime 2008-09-15T15:53:00+05:00
# datetime.date 2008-09-15.2008-09-15.
# datetime.time 14:23:55.003
# datetime.timedelta
# frozenset En solicitudes y respuestas, se trata de la misma manera que un set El esquema generado especificará que los setvalores son únicos (usando los esquemas JSON uniqueItems
# bytes
# Decimal

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID, # tiene que coincidir con un UUID
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None),
):
    start_process = start_datetime + process_after # fechas calcular
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
