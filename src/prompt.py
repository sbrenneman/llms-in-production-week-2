PROMPT = """
You will be given a prompt which you will have to translate to valid SQL.
Here is the request: ${query}

Approach this task step by step:
1. Identify the names of the tables and columns from which would general be used in a DB that could answer the query.
3. Write an SQL query to satisfy the request using those names.
4. Double check that the query makes sense, uses appropriate names, uses appropriate SQL syntax. And make sure it is simple -- doesn't worry about edge cases and doesn't use naming aliases.  If not, modify to meet these requirements.
5. In your response, provide only the SQL statement as a string without any markup or anything else.

${gr.complete_json_suffix_v3}
"""
