# 1.1.0 — startup research (19.10.2026)

Новый, седьмой скилл. Шесть существующих скиллов, contract.md, общие схемы,
рендерер и шаблоны отчётов НЕ менялись.

1. `skills/spytrend-startup-research/` — `SKILL.md`, `agents/openai.yaml`,
   `references/report-template.{md,html}`. Четыре режима: профиль компании
   (`search_startups` → `get_startup`, по желанию `search_startup_news` и
   `get_startup_ads`), сравнение 2–4 компаний (`compare_startups`), поиск
   компании вне каталога (`lookup_startup`), заказ отчёта (`create_company_report`, 1 отчёт из месячной квоты, объекты не списываются; `retry_company_report`, `cancel_company_report`), чтение своих отчётов
   (`list_company_reports` → `get_company_report`).
2. Перед каждым платным вызовом — бесплатный `estimate_cost` с теми же
   аргументами; пользователю называется максимум объектов и остаток. Отчёты
   читаются бесплатно. Пропуск = unknown, не 0; сумма раунда — весь раунд;
   люди — публичные записи без контактов; связь рекламы и раундов — корреляция.
3. `schemas/startup-research.input.json` — закрытая схема аргументов:
   `mode` (обязателен: profile | compare | lookup | reports), `company`,
   `companies`, `country`, `include_people`, `output_mode`, `language`.
4. `manifest.json` — версия 1.1.0, запись нового скилла (описание равно тексту
   frontmatter; параметры и поля ответа сверены со схемами инструментов сервера
   на коммите 0021297).
5. Требуется тариф Startups Business; оплата в объектах Startups, не в токенах.
