-- Ba step s15 và người nói (không phân loại tay). Chạy: duckdb kb/data/kb.duckdb < engine/recipes/s15-idea-filter-criteria.extra.sql
select substr(s.video_id,1,6) as v, s.case_id, s.ts, s.stage, s.what from steps s where s.tactic = 's15-idea-filter-criteria' order by s.video_id;
-- người nói trong ba video
select substr(video_id,1,6) as v, speakers from videos where video_id in (select video_id from steps where tactic = 's15-idea-filter-criteria');
-- bằng chứng nhu cầu của case Kaching Bundles (demand_kind, demand_what)
select demand_kind, demand_what from cases where video_id like 'vLLBzU%' and case_id = 'kaching-bundles';
-- lợi thế Erikas nêu
select value, what from advantages where video_id like 'vLLBzU%' and case_id = 'kaching-bundles';
