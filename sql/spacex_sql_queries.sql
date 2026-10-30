-- SpaceX launch analysis - key SQL queries (SQLite)
-- Database: data/spacex.db, table: SPACEXTBL

-- Unique launch sites
SELECT DISTINCT LaunchSite FROM SPACEXTBL;

-- First 5 launches from CCAFS
SELECT * FROM SPACEXTBL WHERE LaunchSite LIKE 'CCA%' LIMIT 5;

-- Total NASA payload (kg)
SELECT SUM(PayloadMass) AS TotalNASA FROM SPACEXTBL WHERE Customer = 'NASA';

-- Average payload of F9 v1.1 (kg)
SELECT AVG(PayloadMass) AS AvgV11 FROM SPACEXTBL WHERE BoosterVersion = 'F9 v1.1';

-- First ground-pad landing
SELECT MIN(Date) AS MinDate, LandingOutcome, LaunchSite FROM SPACEXTBL WHERE LandingOutcome LIKE 'Success (ground pad)';

-- Drone-ship successes, 4000-6000 kg
SELECT BoosterVersion, PayloadMass, LandingOutcome FROM SPACEXTBL WHERE LandingOutcome = 'Success (drone ship)' AND PayloadMass BETWEEN 4000 AND 6000;

-- Mission outcome counts
SELECT CASE WHEN Class = 1 THEN 'Success' ELSE 'Failure' END AS Mission_Outcome, COUNT(*) AS COUNT FROM SPACEXTBL GROUP BY Class;

-- Heaviest payload
SELECT BoosterVersion, PayloadMass, Orbit FROM SPACEXTBL WHERE PayloadMass = (SELECT MAX(PayloadMass) FROM SPACEXTBL);

-- 2015 drone-ship failures
SELECT Date, BoosterVersion, LaunchSite, LandingOutcome FROM SPACEXTBL WHERE LandingOutcome = 'Failure (drone ship)' AND strftime('%Y', Date) = '2015';

-- Landing outcome rank 2010-2017
SELECT LandingOutcome, COUNT(*) AS COUNT FROM SPACEXTBL WHERE Date BETWEEN '2010-06-04' AND '2017-03-20' GROUP BY LandingOutcome ORDER BY COUNT DESC;