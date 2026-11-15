-- Đếm step s12 nhắc AI mới / API-nền tảng-sự kiện (từ khoá trên what + tactic_note, hai nhóm chồng lấn). Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s12-timing-shift.extra.sql
select count(*) as steps,
       sum(case when regexp_matches(what || ' ' || coalesce(tactic_note,''), '\bAI\b|ChatGPT|Gemini|Suno|Davinci|LLM|OpenAI|OpenClaw', 'i') then 1 else 0 end) as nhac_ai,
       sum(case when regexp_matches(what || ' ' || coalesce(tactic_note,''), 'API|iOS|marketplace|tính năng|Instagram|Skype|Notion', 'i') then 1 else 0 end) as nhac_api_nen_tang_su_kien
from steps where tactic = 's12-timing-shift';
-- theo năm video
select substr(v.date, 1, 4) as nam, count(*) as steps from steps s join videos v using(video_id) where s.tactic = 's12-timing-shift' group by 1 order by 1;
