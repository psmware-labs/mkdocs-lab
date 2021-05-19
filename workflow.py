"""
Note: You can disable this behavior with the `replace_admonitions` option.
    To prevent `pytkdocs` from converting sections to admonitions,
    use the `replace_admonitions`:

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```

    ```md
    ::: workflow
        selection:
          docstring_style: google  # this is the default
          docstring_options:
            replace_admonitions: no
    ```

    So meta!
"""
