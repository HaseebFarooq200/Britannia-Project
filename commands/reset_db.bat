REM --------------------------- RESETTING DATABASE ------------------------------
python .\scripts\reset_db.py
REM --------------------------- INITIALIZING MIGRATION ------------------------------
call .\commands\migrate.bat
@REM REM --------------------------- INITIALIZING SEED ------------------------------
@REM call .\commands\windows\seed.bat
