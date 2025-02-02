import pytest


@pytest.mark.sphinx(testroot='basic')
def test_callouts(app):
    app.build()

    content = (app.outdir / 'index.html').read_text()
    assert '<span class="code-block-callouts"><span>1</span>  </span>' in content
    assert '<span class="code-block-callouts"><span>2</span>  </span>' in content

    assert ('<ol class="arabic simple code-block-callouts">\n'
            '<li><p>Definition of the “hello” function</p></li>\n'
            '<li><p>It will return a string “world” as a return value</p></li>\n'
            '</ol>\n') in content
