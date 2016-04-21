from rest_framework.test import APITestCase
from rest_framework import status


class ProjectAPITestCase(APITestCase):
    fixtures = ['data/course.json', 'data/group.json', 'data/skill.json', 'data/user.json', 'data/skill.json',
                'data/project_data.json', 'data/project_platform.json', 'data/project_target_device.json', 'data/module.json', 'data/exemplar_project_proposal.json']

    def test_add_project(self):
        data = {
            'brief': "brief",
            'company_name': "Big Company",
            'company_video': "http://vimeo.com",
            'data': [2, 3],
            'desired_end_date': "2015-12-30",
            'desired_start_date': "2015-10-08",
            'ip_agreement': "http://ip.com",
            'mentors': [],
            'module': 1,
            'platform': [4, 5],
            'resources_provided': "resources",
            'scope': "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perferendis quam nisi itaque quo, labore fuga enim nihil eius unde ex eligendi consequuntur expedita repellendus, dignissimos nostrum neque assumenda quidem aut!",
            'skills_needed': [4],
            'skills_practiced': [4],
            'student_needed': 10,
            'target_device': [],
            'term': 1,
            'terms_agreement': "http://terms.com",
            'title': "Project Title",
            'creator': 1,
            'target_device': [1, 2]
        }
        response = self.client.post('/api/1/projects/', data, format="json")
        print response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
