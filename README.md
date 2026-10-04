# Навыки для Codex

`task-model-router` подбирает модель и уровень усилия под задачу с учётом возможностей, цены и бюджета. `subagent-manager` координирует делегированную работу и перед каждым назначением использует `task-model-router`. Установите навыки в соседние каталоги, чтобы менеджер находил роутер.

## Установка

Можно попросить Codex: `$skill-installer Установи оба навыка из https://github.com/Rattlhead/codex-agent-skills по путям skills/task-model-router и skills/subagent-manager`.

Для ручной установки клонируйте репозиторий и скопируйте оба навыка. Команды остановятся, если любой навык уже установлен:

```sh
git clone https://github.com/Rattlhead/codex-agent-skills.git
cd codex-agent-skills
(
for name in task-model-router subagent-manager; do
  if [ -e "$HOME/.codex/skills/$name" ] || [ -L "$HOME/.codex/skills/$name" ]; then
    echo "Уже существует: ~/.codex/skills/$name — остановка" >&2
    exit 1
  fi
done
mkdir -p "$HOME/.codex/skills"
cp -R skills/task-model-router skills/subagent-manager "$HOME/.codex/skills/"
)
```

После установки начните новый ход в Codex. По умолчанию навыки могут применяться автоматически; явные вызовы приведены ниже.

## Примеры

- `$task-model-router Оцени задачу и порекомендуй модель и уровень усилия.`
- `$subagent-manager Разбей эту задачу на независимые части и координируй их выполнение.`

Указанные в навыке цены — датированный снимок. Доступность моделей и усилий определяйте по схеме текущего инструмента.
