# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'HIT-SCC'
copyright = '2024, HIT-SCC Team'
author = 'HIT-SCC Team'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'

# html_theme_options = {
#     # 主题的其他配置选项
#     "features": ["navigation.expand"],  # 示例选项，根据文档调整
#     "font": {"text": "Roboto", "code": "Roboto Mono"},  # 示例选项，根据文档调整
#     "plugins": ["sphinx_immaterial"],  # 示例选项，根据文档调整
#     "icon": {"repo": "fontawesome/brands/github"},  # 示例选项，根据文档调整
#     "repo_url": "https://github.com/HIT-SCC/scc.hit.edu.cn/",  # 示例选项，根据文档调整
#     "toc_title": "Table of Contents",  # 示例选项，根据文档调整
#     "toc_title_is_page_title": True,  # 示例选项，根据文档调整
# }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
