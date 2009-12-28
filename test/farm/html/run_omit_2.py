def html_it():
    """Run coverage and make an HTML report for main."""
    import coverage
    cov = coverage.coverage()
    cov.start()
    import main
    cov.stop()
    cov.html_report(directory="../html_omit_2", omit_prefixes=["m1"])

runfunc(html_it, rundir="src")

# HTML files will change often.  Check that the sizes are reasonable,
#   and check that certain key strings are in the output.
compare("gold_omit_2", "html_omit_2", size_within=10, file_pattern="*.html")
clean("html_omit_2")