# Forbidden Files & Directories

The following directories and files are locked out of normal execution. No build agent may read or write files within these paths unless explicitly approved in the active task's authority snapshot.

* `/config/secrets/**/*`
* `/.env`
* `/auth/**/*`
* `/database/migrations/**/*`
