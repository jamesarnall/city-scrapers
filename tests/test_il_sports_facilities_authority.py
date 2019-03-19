from datetime import datetime
from os.path import dirname, join

import pytest
from freezegun import freeze_time
from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.utils import file_response

from city_scrapers.spiders.il_sports_facilities_authority import IlSportsFacilitiesAuthoritySpider

test_response = file_response(
    join(dirname(__file__), "files", "il_sports_facilities_authority.html"),
    url="https://www.isfauthority.com/governance/board-meetings/",
)
spider = IlSportsFacilitiesAuthoritySpider()

test_para = """Board Meeting 12.6.2018 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/December-Board-Meeting-Agenda.pdf" target="_blank" rel="noopener">Agenda</a><br>
Board Meeting 9.20.2018 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/9-20-2018-Board-Meeting-Agenda.pdf" target="_blank" rel="noopener">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/9-20-2018-Board-Meeting-Minutes-1.pdf" target="_blank" rel="noopener">Minutes</a><br>
Audit, Finance and Investment Committee Meeting 9.20.2018 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/09/9-20-2018-Board-Meeting-Agenda.pdf" target="_blank" rel="noopener">Agenda &amp; Minutes</a><br>
Board Meeting 5.10.2018 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/06/May-Board-Meeting-Agenda.pdf" target="_blank" rel="noopener">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/5-9-2018-Board-Meeting-Minutes.pdf" target="_blank" rel="noopener">Minutes</a><br>
Board Meeting 2.15.2018 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/02/AGENDA-02.15.2018.pdf" target="_blank" rel="noopener">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/12/Feb-Board-Meeting-Minutes.pdf" target="_blank" rel="noopener">Minutes</a><br>
Executive Committee Meeting 1.31.2018 <a href="https://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/01/ECM-AGENDA-1-31-18.pdf" target="_blank" rel="noopener">Agenda</a><br>
Board Meeting  12.07.2017 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2017/12/Board-Meeting-Agenda-12.07.2017.pdf" target="_blank" rel="noopener">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2018/02/Board-Meeting-Minutes-12.07.2017.pdf" target="_blank" rel="noopener">Minutes</a><br>
Audit Finance and Investment Committee Meeting 11.20.2017 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2017/12/AFI-Agenda-11-20-17.pdf" target="_blank" rel="noopener">Agenda</a><br>
Board Meeting 9.21.2017 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2017/09/Agenda-9.21.2017.pdf" target="_blank" rel="noopener">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2017/12/Board-Meeting-Minutes-09.21.2017.pdf" target="_blank" rel="noopener">Minutes</a><br>
Board Meeting 5.18.2017 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2017/10/Board-Meeting-Agenda-5.18.2017-1.pdf" target="_blank" rel="noopener">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2017/10/Approved-Minutes-from-May-18-2017.pdf" target="_blank" rel="noopener">Minutes</a><br>
Board Meeting 4.18.2017 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/Board-Meeting-Agenda-April-2017.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2017/06/April-18-2017.pdf" target="_blank" rel="noopener noreferrer">Minutes</a><br>
Board Meeting 12.12.2016 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/SKM_C554e16120712030.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/SKM_C554e1704241416012.12.161.pdf">Minutes</a><br>
Board Meeting 8.24.2016 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/AGENDA.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/8-24-16-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 5.26.2016 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/AGENDA_May.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/5.26.16-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 2.9.2016 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/02/ISFA-Board-Agenda-020516.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/2-9-16-Board-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 12.8.2015 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2015/05/AGENDA-12-8-15.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/12-8-15-Board-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 9.30.2015 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2015/05/Agenda093015.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/9-30-15-Board-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 5.27.2015 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2015/05/052715-AGENDA.pdf" target="_blank" rel="noopener noreferrer">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/5-27-15-Board-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 3.12.2015 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2015/05/AGENDA-031215.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/3-12-15-Board-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 12.8.2014 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/12.8.14-Agenda.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/12-8-14-Board-Minutes_Redacted.pdf">Minutes</a><br>
Board Meeting 5.28.2014 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/5.28.14-Agenda.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/5-28-14-Board-Minutes_Redacted.pdf">Minutes</a><br>
Audit Finance and Investment Committee Meeting 5.2.2014 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/meeting-agendas/www.isfauthority.com/assets/agenda-5-2-14.docx">Agenda</a><br>
Board Meeting 2.27.2014 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2015/12/AGENDA-022714.pdf">Agenda</a> &amp; <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/07/2-27-14-Board-Minutes_Redacted.pdf">Minutes</a><br>
Construction Committee 9.17.2013 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/meeting-agendas/www.isfauthority.com/assets/agenda-9-17-13.docx">Agenda</a><br>
Audit, Finance &amp; Investment Committee Meeting 8.20.2013 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/wp-content/uploads/2016/02/082013-AGENDA.doc">Agenda</a><br>
Audit, Finance &amp; Investment Committee Meeting 1.16.2013 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/assets/1-16-13-agenda.pdf">Agenda</a><br>
Construction Committee 2.11.2013 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/assets/construction-committee_2.11.13.pdf">Agenda</a><br>
Construction Committee 5.13.2013 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/assets/construction-committee_5.13.13.pdf">Agenda</a><br>
Special Board Meeting 5.21.2013 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/assets/agenda_5.12.pdf">Agenda</a><br>
Audit, Finance &amp; Investment Committee Meeting 6.6.2013 <a href="http://236c3m49r38mg7ixa39zqru1-wpengine.netdna-ssl.com/assets/agenda-6-6-13.pdf">Agenda</a>"""


freezer = freeze_time("2019-02-08")
freezer.start()

# parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()


# def test_tests():
#     print("Please write some tests for this spider or at least disable this one.")
#     assert False


"""
Uncomment below
"""


def test_get_paragraph_of_meetings():
    para = spider._get_paragraph_of_meetings(test_response)
    assert para == test_para

def test_get_list_of_meetings_from_inner_paragraph():
    meetings = spider._get_meetings_from_paragraph(test_para);
    assert len(meetings) == 30


# def test_get_correct_no_of_items():
#     assert len(parsed_items) == 30

# def test_title():
#     assert parsed_items[0]["title"] == "EXPECTED TITLE"


# def test_description():
#     assert parsed_items[0]["description"] == "EXPECTED DESCRIPTION"


# def test_start():
#     assert parsed_items[0]["start"] == datetime(2019, 1, 1, 0, 0)


# def test_end():
#     assert parsed_items[0]["end"] == datetime(2019, 1, 1, 0, 0)


# def test_time_notes():
#     assert parsed_items[0]["time_notes"] == "EXPECTED TIME NOTES"


# def test_id():
#     assert parsed_items[0]["id"] == "EXPECTED ID"


# def test_status():
#     assert parsed_items[0]["status"] == "EXPECTED STATUS"


# def test_location():
#     assert parsed_items[0]["location"] == {
#         "name": "EXPECTED NAME",
#         "address": "EXPECTED ADDRESS"
#     }


# def test_source():
#     assert parsed_items[0]["source"] == "EXPECTED URL"


# def test_links():
#     assert parsed_items[0]["links"] == [{
#       "href": "EXPECTED HREF",
#       "title": "EXPECTED TITLE"
#     }]


# def test_classification():
#     assert parsed_items[0]["classification"] == NOT_CLASSIFIED


# @pytest.mark.parametrize("item", parsed_items)
# def test_all_day(item):
#     assert item["all_day"] is False
