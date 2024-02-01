# pytest_practice
Pytest code along practice

Tutorial video: [Learn pytest in 6 Hours⏰ | Complete pytest framework Tutorial |](LambdaTesthttps://youtu.be/KZstMSOHIvQ?si=8slCvoL_t_mhguqg)

### Tips
```pytest -rA --verbose``` - best way to run tests because it is informative

```pytest -k lambdatest -rA -v``` - will run all tests that contain string "lambdatest"

```pytest -k [fileName.py]::[test_nameInTheFile] -rA -v``` - will run a specific test from a specific file
