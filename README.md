# Навыки для Codex

`task-model-router` оценивает сложность и бюджет задачи. Он выбирает модель и усилие. Он решает, справится ли основной агент сам или нужны субагенты. `subagent-manager` выполняет это решение. Он делит работу, координирует исполнителей и принимает результаты. Установите оба навыка в соседние каталоги, чтобы менеджер находил роутер.

`task-token-retrospective` после крупной задачи кратко разбирает потери токенов. Он проверяет правила проекта и причины их неприменения. Если нужна правка, он показывает точный текст. Он меняет инструкции проекта только после явного одобрения этой правки пользователем. При отсутствии счётчиков он не заявляет точные расходы или экономию.

Переиспользование агента разрешено только для продолжения исходного среза в том же контексте. Новая область, самостоятельный результат или независимое ревью требуют нового агента; подробные критерии — в [правиле переиспользования](skills/subagent-manager/SKILL.md#reuse-within-the-original-slice).

## Установка

Можно попросить Codex: `$skill-installer Установи три навыка из https://github.com/Rattlhead/codex-agent-skills по путям skills/task-model-router, skills/subagent-manager и skills/task-token-retrospective`.

Для ручной установки клонируйте репозиторий и скопируйте три навыка. Команды остановятся, если любой навык уже установлен:

```sh
git clone https://github.com/Rattlhead/codex-agent-skills.git
cd codex-agent-skills
(
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
for name in task-model-router subagent-manager task-token-retrospective; do
  if [ -e "$skill_root/$name" ] || [ -L "$skill_root/$name" ]; then
    echo "Уже существует: $skill_root/$name — остановка" >&2
    exit 1
  fi
done
mkdir -p "$skill_root"
cp -R skills/task-model-router skills/subagent-manager skills/task-token-retrospective "$skill_root/"
)
```

После установки начните новый ход в Codex. По умолчанию навыки могут применяться автоматически; явные вызовы приведены ниже.

## Обновление

В каталоге клонированного репозитория выполните команды ниже. Они загрузят новую версию, сохранят резервную копию установленных навыков и обновят их. Новые навыки будут установлены. Локальные правки заменяются версией из репозитория; копия остаётся в `~/.codex/skill-backups/`.

```sh
(
set -eu
git pull --ff-only
skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
backup_dir="${CODEX_HOME:-$HOME/.codex}/skill-backups/$(date +%Y%m%d-%H%M%S)-$$"
for name in task-model-router subagent-manager task-token-retrospective; do
  test -f "skills/$name/SKILL.md"
  test ! -L "$skill_root/$name"
  if [ -e "$skill_root/$name" ]; then
    test -d "$skill_root/$name"
  fi
done
mkdir -p "$backup_dir"
for name in task-model-router subagent-manager task-token-retrospective; do
  if [ -d "$skill_root/$name" ]; then
    cp -R "$skill_root/$name" "$backup_dir/$name"
  fi
done
for name in task-model-router subagent-manager task-token-retrospective; do
  mkdir -p "$skill_root/$name"
  rsync -a --checksum --delete "skills/$name/" "$skill_root/$name/"
done
echo "Обновлено. Резервная копия: $backup_dir"
)
```

Начните новый ход в Codex, чтобы использовать обновлённые навыки. Если потребуется восстановление, скопируйте содержимое нужной резервной версии обратно в соответствующие каталоги навыков.

## Примеры

- `$task-model-router Оцени задачу и порекомендуй модель и уровень усилия.`
- `$subagent-manager Разбей эту задачу на независимые части и координируй их выполнение.`
- `$task-token-retrospective Кратко разбери потери токенов в завершённой задаче и предложи исправления правил.`

Автовыбор навыка не гарантирует его запуск после каждой крупной задачи. Если требуется обязательный разбор, попросите добавить в проектный `AGENTS.md` правило: «После завершения крупной задачи применяй $task-token-retrospective. Правки инструкций проекта вноси только после явного одобрения показанной правки». Добавление этого правила требует вашего подтверждения.

Указанные в навыке цены — датированный снимок. Доступность моделей и усилий определяйте по схеме текущего инструмента.
