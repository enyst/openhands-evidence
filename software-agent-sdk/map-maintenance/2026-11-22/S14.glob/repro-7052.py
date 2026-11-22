import os, tempfile, shutil
from openhands.tools.glob.definition import GlobAction
from openhands.tools.glob.impl import GlobExecutor
d = os.path.realpath(tempfile.mkdtemp()); os.makedirs(f"{d}/src/sub"); open(f"{d}/src/app.ts","w").close(); open(f"{d}/src/sub/b.ts","w").close()
print("rg:", shutil.which("rg"), "cwd:", os.getcwd(), "search:", d)
ex = GlobExecutor(working_dir=d)
for pat in ["src/*.ts", "src/**/*.ts", "src/app.ts", "*.ts", "**/*.ts"]:
    obs = ex(GlobAction(pattern=pat))
    print(f"{pat!r}: files={obs.files} error={obs.is_error}")
print("cwd after:", os.getcwd())
