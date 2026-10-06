# Навыки для Codex

`task-model-router` подбирает модель и уровень усилия под задачу с учётом возможностей, цены и бюджета. `subagent-manager` координирует делегированную работу и перед каждым назначением использует `task-model-router`. Установите навыки в соседние каталоги, чтобы менеджер находил роутер.

Переиспользование агента разрешено только для продолжения исходного среза в том же контексте. Новая область, самостоятельный результат или независимое ревью требуют нового агента; подробные критерии — в [правиле переиспользования](skills/subagent-manager/SKILL.md#reuse-within-the-original-slice).

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

## Обновление

В каталоге клонированного репозитория выполните команды ниже. Они загрузят новую версию, сохранят резервную копию установленных навыков и обновят оба вместе. Локальные правки заменяются версией из репозитория; копия остаётся в `~/.codex/skill-backups/`.

```sh
(
set -eu
git pull --ff-only
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
backup_dir="${CODEX_HOME:-$HOME/.codex}/skill-backups/$(date +%Y%m%d-%H%M%S)-$$"
for name in task-model-router subagent-manager; do
  test -f "skills/$name/SKILL.md"
  test -d "$skill_root/$name"
  test ! -L "$skill_root/$name"
done
mkdir -p "$backup_dir"
for name in task-model-router subagent-manager; do
  cp -R "$skill_root/$name" "$backup_dir/$name"
done
for name in task-model-router subagent-manager; do
  rsync -a --checksum --delete "skills/$name/" "$skill_root/$name/"
done
echo "Обновлено. Резервная копия: $backup_dir"
)
```

Начните новый ход в Codex, чтобы использовать обновлённые навыки. Если потребуется восстановление, скопируйте содержимое нужной резервной версии обратно в соответствующие каталоги навыков.

## Примеры

- `$task-model-router Оцени задачу и порекомендуй модель и уровень усилия.`
- `$subagent-manager Разбей эту задачу на независимые части и координируй их выполнение.`

Указанные в навыке цены — датированный снимок. Доступность моделей и усилий определяйте по схеме текущего инструмента.
