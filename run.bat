make clean && make html && rmdir /s /q "./docs" && xcopy "./build/html" "./docs" /E && echo > docs/.nojekyll && mkdir "./docs/_pdf" &&xcopy "./source/pdf" "./docs/_pdf" /E