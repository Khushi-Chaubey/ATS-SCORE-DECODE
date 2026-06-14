
# Insurance Data Analysis 

Here is the adapted text content for your Power BI project, analyzing and reflecting the data from the PRISM Insurance Dashboard provided in the document.



## Problem Statement

This dashboard helps PRISM Insurance Pvt. Ltd.  understand their policyholders and claims processes better. It provides visibility into claim statuses, financial metrics, demographic distributions, and overall customer sentiment based on direct feedback. Through sentiment analysis and status tracking, the company can identify critical areas for improvement.

Since a significant portion of claims are 'Rejected' (4.4K) compared to 'Settled' (3.4K) , and the majority of customer feedback falls under 'Needs improvement' (58 out of 97 reviews), the company must focus on improving the claims settlement process, enhancing policy transparency, and addressing user experience issues with their online portal.
## Steps Followed -

**Step 1:** Load data into Power BI Desktop, utilizing datasets containing policyholder details, claims history, and customer feedback.

**Step 2:** Open Power Query Editor & in the view tab under the Data preview section, check "column distribution", "column quality" & "column profile" options.

 **Step 3:** Select "column profiling based on entire dataset" to ensure all rows are evaluated.

 **Step 4:** Address empty values in the dataset. For instance, `ClaimDate` and `ClaimAmount` might contain nulls or `0.00` values specifically for claims that have a `ClaimStatus` of 'Rejected' or 'Pending'.



**Step 5:** Create visual filters (Slicers) for fields such as "Policy Type" , "Claim Status" , and "Age Group".


 
**Step 6:** Add key performance indicator (KPI) card visuals to the canvas to represent high-level financials: Total Premium Amount (5.97M) , Total Coverage Amount (600.33M) , and Total Claim Amount (16.90M).


**Step 7:** Add a Donut Chart to visualize the Count of Active vs. Inactive Policies.


**Step 8:** Add a Bar Chart representing Premium Amount by Policy Type  (Travel, Health, Auto, Life, Home) .



**Step 9:** Add an Area/Column chart to represent the Number of Claims by Claim Status , visualizing the distribution of Rejected, Settled, and Pending claims.



**Step 10:** Create a Line Chart to track Claim Status by Age Group (Young Adult, Adult, Elder).


**Step 11:** Incorporate Sentiment Analysis visuals. A Word Cloud was used to highlight frequent terms in customer feedback (e.g., "process", "service", "policy", "website") , and a Bar Chart was created to group Sentiment Scores into categories: Needs Improvement, Good, and Excellent.


**Step 12:** Utilize DAX expressions to group customers by Age Group based on their actual age.


```
  Age Group = 
  IF(Insurance[Age]<=25, "Young Adult",
  IF(Insurance[Age]<=60, "Adult",
  "Elder"))

```



**Step 13:** Create measures for Sentiment Categorization based on the continuous Sentiment Score (-1.0 to 1.0).


```
  Feedback Category = 
  IF(Insurance[Score Sentiment] < 0, "Needs improvement",
  IF(Insurance[Score Sentiment] <= 0.5, "Good",
  "Excellent"))

```

**Step 14:** The report was then formatted with the company logo and published to Power BI Service.


## Insights

A single-page report was created on Power BI Desktop & published to Power BI Service. Following inferences can be drawn from the dashboard:

### [1] Policy & Customer Overview

**Total Policies:** ~10,000 Total
 
**Active Policies:** 5.81K (58.11%) 


 
**Inactive Policies:** 4.19K (41.89%) 


* *Insight:* A significant portion of the customer base holds inactive policies, indicating a potential need for retention or renewal campaigns.



### [2] Financial Metrics

 
**Total Premium Amount:** 2.5M  + 1.2M  + 1.0M  + 0.7M  + 0.6M = 6.0M (Dashboard displays 5.97M overall).



**Total Coverage Amount:** 600.33M 



**Total Claim Amount:** 16.90M 



### [3] Premium by Policy Type

 
**Travel:** 2.5M (Highest revenue driver) 



**Health:** 1.2M 



**Auto:** 1.0M 



**Life:** 0.7M 



**Home:** 0.6M 



### [4] Claims Status Breakdown

 **Total Claims Analyzed:** 10,100

**Rejected:** 4.4K 



**Settled:** 3.4K 



**Pending:** 2.3K 


* *Insight:* The rejection rate is exceptionally high (higher than settled claims). This correlates directly with the negative customer feedback regarding transparency and claim trouble.



### [5] Claims by Demographics (Age Group)


**Adult:** 5.1K Claims 



**Elder:** 3.8K Claims 

 
**Young Adult:** 1.0K Claims 


* *Insight:* The "Adult" demographic files the vast majority of claims, followed closely by the "Elder" demographic.



### [6] Customer Feedback & Sentiment


**Needs Improvement (Negative Score):** 58 Customers 



**Good (Neutral/Positive Score):** 28 Customers 


 
**Excellent (High Positive Score):** 11 Customers 


* *Insight:* Nearly 60% of recorded textual feedback highlights issues. Common complaints include website outages, unexplained premium rate increases, and unclear coverage details. Management must address IT infrastructure (website downtime) and improve policy term transparency to improve these satisfaction metrics.