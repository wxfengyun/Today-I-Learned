#coding=utf-8
''' Simple script to auto-generate the README.md file for a til project.
    NOTE: Someone who wanted to be fancy would actually use a template engine
    for this, but this seemed like a task for which it is best to only require
    python.  This is not a general purpose script, but tailored for the format
    being used for "Today I Learned" repos.
    Apply as a git hook by running the following command in linux:
        cd .git/hooks/ && ln -s ../../createReadme.py pre-commit && cd -
'''
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

HEADER = '''# 日常编程记录 Today I Learned
> 我每天学了点啥 Today I Learned
随手记录每天学习的点滴编程技术，备查使用，也希望能给需要的人带来帮助。
文章都是一些碎片化的记录，不是完整的博客。  

A collection of concise write-ups on small things I learn day to day across a
variety of languages and technologies. These are things that don't really
warrant a full blog post.
'''

FOOTER = '''## 使用方法 Usage
在根目录下执行 `python createReadme.py` 可以自动根据目录结构生成README.md  

After creating a new entry, run `./createReadme.py > README.md` to regenerate
the readme with the new data.
If you are using git, you can install this script as a pre-commit git hook so
that it is autogenerated on each commit.  Use the following command:
    cd .git/hooks/ && ln -s ../../createReadme.py pre-commit && cd -
## 关于 About
此想法的最初来源[jbranchaud/til](https://github.com/jbranchaud/til)  

I shamelessly stole this idea from
[jbranchaud/til](https://github.com/jbranchaud/til) who claims to have stolen
it from others.
## 其他每日记录 Other TIL Collections
* [jbranchaud/til](https://github.com/jbranchaud/til) who claims to have stolen
* [Today I Learned by Hashrocket](https://til.hashrocket.com)
* [jwworth/til](https://github.com/jwworth/til)
* [thoughtbot/til](https://github.com/thoughtbot/til)
* [jima80525/til](https://github.com/jima80525/til)
## 版权信息 License
&copy; 2017-2020 Jim Anderson & 小黄鸡
This repository is licensed under the MIT license. See `LICENSE` for
details.'''


def get_list_of_categories():
    ''' Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" in which there are TILs.'''
    dirs = [x for x in os.listdir('.') if os.path.isdir(x) and
            '.git' not in x]
    return dirs


def get_title(til_file):
    ''' Read the file until we hit the first line that starts with a #
    indicating a title in markdown.  We'll use that as the title for this
    entry. '''
    with open(til_file) as _file:
        for line in _file:
            line = line.strip()
            if line.startswith('#'):
                return line[1:].lstrip()  # text after # and whitespace


def get_tils(category):
    ''' For a given category, get the list of TIL titles. '''
    til_files = [x for x in os.listdir(category)]
    titles = []
    for filename in til_files:
        filename = filename.decode(encoding='gbk')
        fullname = os.path.join(category, filename)
        if (os.path.isfile(fullname)) and fullname.endswith('.md'):
            title = get_title(fullname)
            titles.append((title, fullname))
    return titles


def get_category_dict(category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_tils(category)
        categories[category] = titles
        count += len(titles)
    return count, categories


def print_file(category_names, count, categories):
    ''' Now we have all the information, print it out in markdown format. '''
    with open('README.md', 'w') as file_:
        file_.write(HEADER)
        file_.write('\n')
        file_.write('_{0} TILs and counting..._'.format(count))
        file_.write('\n')
        file_.write('''
---
### Categories
''')
        # print the list of categories with links
        for category in sorted(category_names):
            file_.write('* [{0}](#{1})\n'.format(category.capitalize(),
                                                 category))

        # print the section for each category
        file_.write('''
---
''')
        for category in sorted(category_names):
            file_.write('### {0}\n'.format(category.capitalize()))
            file_.write('\n')
            tils = categories[category]
            for (title, filename) in sorted(tils):
                file_.write('- [{0}]({1})\n'.format(title, str(filename)))
            file_.write('\n')

        file_.write(FOOTER)


def create_readme():
    ''' Create a TIL README.md file with a nice index for using it directly
        from github. '''
    category_names = get_list_of_categories()
    count, categories = get_category_dict(category_names)
    print_file(category_names, count, categories)

if __name__ == '__main__':

    create_readme()
    #os.system('git add README.md')