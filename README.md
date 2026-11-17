# Сборка пакетов TeX Live в Docker

В учебном проекте я подготовил два сценария сборки Linux-пакетов. Для Ubuntu собрал схему упаковки `xprintlen` в DEB через `dpkg-deb`, для ROSA — `topiclongtable` в RPM через `rpmbuild`. В первом слое Docker скачивает исходные архивы из CTAN и собирает пакет, во втором устанавливает его и при запуске выводит информацию из пакетного менеджера.

## Сборка и проверка

Нужны Docker с Compose и доступ к зеркалу CTAN и репозиториям базовых образов.

```sh
docker compose build
docker compose run --rm xprintlen-deb
docker compose run --rm topiclongtable-rpm
```

В `deb/control` находятся метаданные DEB, а в `rpm/texlive-topiclongtable.spec` — инструкция сборки RPM. Аргумент `CTAN_ARCHIVE` позволяет выбрать зеркало с деревом архивов TeX Live.

Пакеты TeX Live распространяются по лицензиям их авторов. [xprintlen на CTAN](https://ctan.org/pkg/xprintlen) · [topiclongtable на CTAN](https://ctan.org/pkg/topiclongtable)
