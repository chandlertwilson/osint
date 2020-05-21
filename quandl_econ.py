import quandl
import pandas as pd
quandl.ApiConfig.api_key = 'API_KEY'

Code_Examples
#OECD Rate of capacity utilization UK, Hong Kong. Same code but country code HKG and GBR are inserted.

oecd =quandl.get(['OECD/MEI_BTS_COS_BSCURT_GBR_BLSA_A', "OECD/MEI_BTS_COS_BSCURT_KHG_BLSA_A"],  collapse="monthly", start_date="2010-01-01", end_date="2020-02-04") 

#FED Price Index Urban Consumers, Potential GDP
fed=quandl.get(['FRED/CPIAUCSL','FRED/GDPPOT'],collapse="daily", start_date="2020-01-01", end_date="2020-03-23") 

#ONS - All ONS data in one pul

ons=quandl(['UKONS/AEI', 'UKONS/AM', 'UKONS/BB', 'UKONS/BERD', 'UKONS/CAPSTK', 'UKONS/CT', 'UKONS/CNXV', 'UKONS/DIOP', 'UKONS/DRSI', 'UKONS/EDP1', 'UKONS/EDP2', 'UKONS/EDP3', 'UKONS/EDP4', 'UKONS/EMP', 'UKONS/GDPO', 'UKONS/GERD', 'UKONS/IOS1', 'UKONS/LMS', 'UKONS/MM17', 'UKONS/MM19', 'UKONS/MM22', 'UKONS/MM23', 'UKONS/MQ10', 'UKONS/MQ5', 'UKONS/MRET', 'UKONS/NBS', 'UKONS/NFBS', 'UKONS/OTT', 'UKONS/PB', 'UKONS/PGDP', 'UKONS/PN2', 'UKONS/PNBP', 'UKONS/PPI', 'UKONS/PRDY', 'UKONS/PROF', 'UKONS/PSE', 'UKONS/PUSF', 'UKONS/QNA', 'UKONS/RGVA', 'UKONS/RGHI', 'UKONS/SDQ7', 'UKONS/SPPI', 'UKONS/SRS', 'UKONS/TOPSI', 'UKONS/UKEA', 'UKONS/UNEM', 'UKONS/WGDP'],collapse="quaterly", start_date="2000-01-01", end_date="2020-05-20")

#WORLDBANK Capital Formation China, Global Public Secotr Debt

world_bank=quandl(['WWDI/CHN_NE_GDI_TOTL_CD','WPSD/WLD_DP_DOD_DECT_CR_GG_CD'],collapse="yearly", start_date="2000-01-01", end_date="2020-02-04") 


#Export CSV
ons.to_csv("file_name.csv")