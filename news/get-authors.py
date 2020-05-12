#!/usr/bin/env python3

"""

Este comando (''script'') navega através do histórico de implementação (''commit'') git (Começando na última etiqueta), recolhe todos os autores das
implementações e cria fragmento para `towncrier`_ tool.

Isto deve ser executado durante o processo de lançamento, antes de gerar as notas de lançamento.

Exemplo::

    $ python get_authors.py

.. _towncrier: https://github.com/hawkowl/towncrier/

Autores:
    Aurelien Bompard
    Michal Konecny
"""

import os
from subprocess import check_output

last_tag = check_output(
    "git tag | sort -n | tail -n 1", shell=True, universal_newlines=True
)
authors = {}
log_range = last_tag.strip() + "..HEAD"
output = check_output(
    ["git", "log", log_range, "--format=%ae\t%an"], universal_newlines=True
)
for line in output.splitlines():
    email, fullname = line.split("\t")
    email = email.split("@")[0].replace(".", "")
    if email in authors:
        continue
    authors[email] = fullname

for nick, fullname in authors.items():
    filename = "{}.author".format(nick)
    if os.path.exists(filename):
        continue
    print(f"Adding author {fullname} ({nick})")
    with open(filename, "w") as f:
        f.write(fullname)
        f.write("\n")
