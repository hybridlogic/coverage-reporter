from tests.testcase import CoverageReporterTestCase

class PathTest(CoverageReporterTestCase):

    def test_patch_filter(self):
        data = self.create_exact_coverage_data({'tests/data/prog3.py' : {'lines'   : [1,2,3,4,5,6,8],
                                                                   'covered' : [1,2,3,6,8]}})
        filter = self.load_plugin('patch')
        filter.patch = 'tests/data/prog3.patch'
        filter.patch_level = 0
        new_data = filter.filter(data)
        path = new_data.canonical_path('tests/data/prog3.py')
        self.assertEqual(new_data.lines[path], set([1,6,8]))
        self.assertEqual(new_data.covered[path], set([1,2,3,6,8]))

    def test_patch_filter_oneline(self):
        data = self.create_exact_coverage_data({'tests/data/oneline.file' : {'lines': [1], 'covered': [1]}})
        filter = self.load_plugin('patch')
        filter.patch = 'tests/data/oneline.patch'
        filter.patch_level = 1
        new_data = filter.filter(data)
        path = new_data.canonical_path('tests/data/oneline.file')
        self.assertEqual(new_data.lines[path], set([1]))
        self.assertEqual(new_data.covered[path], set([1]))
