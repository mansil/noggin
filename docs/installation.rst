============
Instalação
============

Isto abrange a instalação num contexto de desenvolvimento.

.. nota:: **TODO**: Abrange a instalação do utilizador final aqui.


* Utilize `containerdev`_ do projeto relrod para desenvolvimento. (Ou não, mas pelo menos siga estes passos no "Dockerfile" para configurar o seu próprio ambiente.)
* Copie o seu servidor de IPA ``/etc/ipa/ca.crt`` para ``.containerdev-public/ipa01``
* Copie ``noggin.cfg.default`` para ``noggin.cfg`` e edite de acordo. Está no .gitignore, e assim, está seguro para colocar lá o que pretender.

  * A combinação de ``FREEIPA_ADMIN_USER``/``FREEIPA_ADMIN_PASSWORD`` não precisa der um utilizador administrador completo. Este só precisa de ser um utilizador numa função com privilégios que tenha as permissões seguintes:

    * Sistema: Adicionar Utilizador ao grupo predefinido
    * Sistema: Adicionar Utilizadores
    * Sistema: Alterar a palavra-passse do Utilizador
    * Sistema: Ler a Definição UPG

* Ter instalado ``podman``
* Executar ``containerdev-build && containerdev``
* De dentro da consola do "container", executar ``flask run -h0``
* No seu navegador local vá para http://localhost:5000

.. _containerdev: https://github.com/relrod/containerdev
