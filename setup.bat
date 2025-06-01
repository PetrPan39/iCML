@echo off
REM ============== SPUSTENI CML/EVO SYSTEMU ==============

REM 1. Aktivace virtuálního prostředí
call venv\Scripts\activate

REM 2. Načtení proměnných prostředí (pokud používáš .env, doporučuji python-dotenv - načte si je program sám)

REM 3. Spuštění Dockeru pro Astra DB (Cassandra) - pokud používáš Astra cloud, tento krok přeskoč
REM docker compose -f docker\docker-compose.yml up -d

REM 4. Spuštění hlavního dashboardu (GUI)
python main_dashboard.py

REM 5. (Nepovinné) - Pozdravení uživatele (provádí již program)
REM echo Systém CML/EVO je připraven. Vítejte!

REM 6. (Nepovinné) - Spuštění dalších služeb, workerů, apod.

REM ============== KONEC ==============
pause