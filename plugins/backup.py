import os
from spanky.plugin import hook
from spanky.plugin.permissions import Permission


@hook.periodic(3600 * 12)
def backup_data():
    os.system(
        'cd storage_data && \
            git add -A && \
            git commit -m "Update data" && \
            git push'
    )

@hook.command(permission=Permission.bot_owner)
def force_backup_data():
    backup_data()
