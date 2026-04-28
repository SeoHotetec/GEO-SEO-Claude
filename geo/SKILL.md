# geo — GEO-first SEO Skill Suite

GEO-first, SEO-supported. Optimize for AI-powered search engines (ChatGPT,
Claude, Perplexity, Gemini, Google AI Overviews) while maintaining traditional
SEO foundations.

## Command routing

Parse the first argument after `/geo` and dispatch to the appropriate sub-skill
or script. All commands follow the pattern `/geo <command> [args]`.

| Command | Skill / Handler |
|---------|----------------|
| `audit <url>` | `geo-audit` skill |
| `quick <url>` | `geo-audit` skill (quick mode) |
| `citability <url>` | `geo-citability` skill |
| `crawlers <url>` | `geo-crawlers` skill |
| `llmstxt <url>` | `geo-llmstxt` skill |
| `brands <url>` | `geo-brand-mentions` skill |
| `platforms <url>` | `geo-platform-optimizer` skill |
| `schema <url>` | `geo-schema` skill |
| `technical <url>` | `geo-technical` skill |
| `content <url>` | `geo-content` skill |
| `report <url>` | `geo-report` skill |
| `report-pdf` | `geo-report-pdf` skill |
| `prospect [...]` | `geo-prospect` skill |
| `proposal [...]` | `geo-proposal` skill |
| `compare [...]` | `geo-compare` skill |
| `gsc [...]` | `geo-gsc` skill — Google Search Console integration |

## GSC sub-commands

When the command starts with `gsc`, delegate to the `geo-gsc` skill:

```
/geo gsc properties   → list all GSC properties
/geo gsc setup        → OAuth2 setup guide
/geo gsc auth         → re-authenticate
```

## Help

If the user runs `/geo` or `/geo help`, display the command table above with a
one-line description for each command.
