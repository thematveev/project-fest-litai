# ЛІТАЙ FEST — Website Design System

## 1. Brand Overview

**Brand:** ЛІТАЙ FEST

**Positioning:** Premium Ukrainian psychology festival.

**Visual direction:** Elegant Ukrainian / Cultural Premium.

### Brand personality

- Elegant
- Premium
- Cultural
- Artistic
- Modern
- Ukrainian
- Emotional
- Sophisticated
- Airy
- Natural
- Inspiring

### Core idea

The visual identity combines contemporary European editorial design with Ukrainian cultural identity.

The website should feel like a high-end cultural magazine or art festival rather than a generic event landing page.

### Avoid

- Generic music-festival aesthetics
- SaaS-style UI
- Corporate visual language
- Nightclub aesthetics
- Wedding-invitation aesthetics
- Excessive traditional Ukrainian ornament
- Excessive gradients
- Excessive rounded cards
- Excessive gold
- Aggressive animations

---

# 2. Logo

The provided ЛІМАЛ FEST logo is the primary visual reference.

Do not redesign or distort the logo.

The logo contains the main visual language of the brand:

- Emerald calligraphic typography
- Warm gold details
- Feather
- Flying bird
- Gold arc
- Gold particles
- Flowing brush strokes
- Organic forms
- Ukrainian tagline

### Logo usage

- Preserve proportions.
- Do not stretch or skew.
- Do not rotate.
- Do not recolor arbitrarily.
- Maintain sufficient clear space.
- Do not place the logo on backgrounds that reduce readability.
- Use the original logo artwork whenever possible.

---

# 3. Visual Language

The website should extend the logo rather than simply place it inside a conventional website.

### Core visual elements

1. Feather
2. Bird
3. Gold Arc
4. Gold Particles
5. Brush Stroke
6. Organic Line
7. Editorial Typography
8. Large Negative Space

These elements should be reusable across the design system.

---

# 4. Color System

## Primary

| Token | HEX | Usage |
|---|---|---|
| Emerald 900 | `#123F39` | Primary text, dark backgrounds |
| Emerald 700 | `#1C5B50` | Primary actions |
| Emerald 500 | `#3F8174` | Secondary UI |
| Mint 100 | `#E8F0E9` | Main background |
| Mint 50 | `#F5F8F4` | Secondary background |

## Gold

| Token | HEX | Usage |
|---|---|---|
| Gold 700 | `#A87320` | Strong accents |
| Gold 500 | `#D5A54A` | Borders, details, icons |
| Gold 300 | `#E8C77D` | Decorative accents |

## Neutral

| Token | HEX | Usage |
|---|---|---|
| White | `#FFFFFF` | Light surfaces |
| Gray 100 | `#F1F3F0` | Subtle surfaces |
| Gray 300 | `#D8DDD8` | Borders |
| Gray 500 | `#89918B` | Secondary text |
| Gray 700 | `#4B544F` | Muted primary text |
| Black | `#17201D` | Highest contrast text |

## Color principles

- Mint is the dominant background.
- Emerald is the dominant UI and typography color.
- Gold is a premium accent.
- White provides contrast and breathing room.
- Gold should never dominate the interface.
- Light gold should not be used for important body text.
- Maintain strong text/background contrast.

---

# 5. Typography

## Display Typeface

**Cormorant Garamond**

Use for:

- Hero headlines
- Major section headings
- Festival name
- Editorial statements
- Quotes
- Emotional visual moments

## UI Typeface

**Manrope**

Use for:

- Navigation
- Body text
- Buttons
- Labels
- Forms
- Dates
- Cards
- Metadata

## Decorative Typeface

Use an elegant italic/script style sparingly.

Possible direction:

- Lora Italic
- Ballet
- Similar elegant script

Script should only be used for short decorative accents.

Do not use script for paragraphs or functional UI.

---

# 6. Typography Scale

## Desktop

| Style | Size | Line Height |
|---|---:|---:|
| Display XL | 96px | 0.95 |
| Display L | 72px | 1.00 |
| H1 | 56px | 1.05 |
| H2 | 44px | 1.10 |
| H3 | 32px | 1.20 |
| H4 | 24px | 1.30 |
| Body Large | 20px | 1.60 |
| Body | 17px | 1.55 |
| Body Small | 14px | 1.50 |
| Caption | 12px | 1.40 |

## Mobile

| Style | Size |
|---|---:|
| Display XL | 52px |
| Display L | 44px |
| H1 | 40px |
| H2 | 32px |
| H3 | 24px |
| Body | 16px |
| Caption | 12px |

### Typography principles

- Large headlines should be expressive.
- Body text should remain highly readable.
- Use serif + sans-serif contrast.
- Avoid too many font weights.
- Keep editorial typography visually dominant.

---

# 7. Grid

## Desktop

```text
Max width: 1280px
Columns: 12
Gutter: 24px
Side padding: 40px
```

## Tablet

```text
Columns: 8
Gutter: 20px
Side padding: 32px
```

## Mobile

```text
Columns: 4
Gutter: 16px
Side padding: 20px
```

### Container

```text
max-width: 1280px
margin: 0 auto
```

---

# 8. Spacing System

Base unit: **4px**

```text
4
8
12
16
24
32
40
48
64
80
96
128
160
```

### Common spacing

```text
Card padding:      24px
Component gap:     16–24px
Section spacing:   96px
Hero spacing:      128px
Mobile section:    64px
```

Use generous whitespace.

Whitespace is a major part of the brand identity.

---

# 9. Border Radius

Use restrained rounding.

```text
Small:  4px
Medium: 8px
Pill:   999px
```

### Principles

- Cards: 4–8px
- Inputs: 4–8px
- Buttons: 999px
- Tags: 999px

Avoid excessive rounded containers.

---

# 10. Shadows

Shadows should be subtle.

Preferred:

```text
0 8px 30px rgba(18, 63, 57, 0.08)
```

Use shadows only when necessary.

Avoid heavy black shadows.

---

# 11. Buttons

## Primary Button

Example:

```text
КУПИТИ КВИТОК
```

Properties:

```text
Background: #1C5B50
Color: #FFFFFF
Height: 52px
Padding: 14px 24px
Radius: 999px
Font: Manrope
Weight: 600
Size: 14px
Letter spacing: 0.04em
```

### States

- Default
- Hover
- Active
- Focus
- Disabled
- Loading

### Hover

Use subtle movement:

```text
Arrow: translateX(4px)
Background: slightly darker emerald
```

---

## Secondary Button

```text
Background: transparent
Border: 1px solid #D5A54A
Color: #123F39
Height: 52px
Radius: 999px
```

---

## Text Button

```text
Дізнатися більше →
```

No background.

Use a subtle gold underline or animated line.

---

## Icon Button

Use for:

- menu
- close
- navigation
- gallery
- media controls

Minimum interactive size:

```text
44 × 44px
```

---

# 12. Header

## Desktop structure

```text
LOGO

Про фестиваль
Програма
Учасники
Локація

КВИТКИ
```

### Initial state

Transparent over Hero.

### Sticky state

```text
background: rgba(245, 248, 244, 0.92)
backdrop-filter: blur(16px)
border-bottom: 1px solid #D8DDD8
```

### Header principles

- Minimal navigation
- Clear hierarchy
- Logo is visually dominant
- Ticket CTA is always easy to find
- Avoid excessive header controls

---

# 13. Mobile Navigation

Mobile header:

```text
LOGO                         MENU
```

Menu opens into a full-screen or large overlay.

Navigation:

```text
Про фестиваль
Програма
Учасники
Локація
Квитки
```

Use large editorial typography for menu items.

Keep the interface simple.

---

# 14. Hero

Hero is the primary visual statement.

## Content

```text
12—15 ВЕРЕСНЯ

ЛІМАЛ FEST

Сила • Опора • Свобода • Спільнота

[ КУПИТИ КВИТОК ]
```

## Layout

Use an asymmetrical editorial composition.

Include:

- Large typography
- Negative space
- Feather
- Bird
- Gold arc
- Gold particles
- Soft brush elements

The Hero should feel like an art festival poster transformed into a digital experience.

---

# 15. Decorative System

## Feather

Primary decorative element.

Use for:

- Hero
- About
- CTA
- Footer
- Section transitions

## Bird

Represents freedom.

Use sparingly.

## Gold Arc

Can be used as:

- Decorative frame
- Divider
- Background element
- Motion element

## Gold Particles

Small gold dots inspired by the logo.

Use as subtle accents.

## Brush Stroke

Soft flowing forms inspired by the feather.

Use with low visual density.

## Organic Line

Thin flowing lines can connect sections visually.

---

# 16. Cards

Cards should feel editorial and premium.

Avoid generic SaaS card design.

## Base Card

```text
Background: #F5F8F4
Border: 1px solid #D8DDD8
Radius: 4px
Padding: 24px
```

## Event Card

```text
IMAGE

12 ВЕРЕСНЯ

Назва події

Короткий опис...

ДЕТАЛЬНІШЕ →
```

## Artist Card

Large portrait photography.

```text
IMAGE

Ім'я

Роль / напрям
```

## Card states

- Default
- Hover
- Active
- Selected
- Disabled

### Hover

```text
Image: scale(1.03)
Arrow: translateX(4px)
```

---

# 17. Program / Timeline

The program should feel editorial rather than like a dashboard.

Example:

```text
12 ВЕРЕСНЯ

18:00    Відкриття

19:00    Концерт

21:00    Спеціальна подія
```

Possible visual elements:

- Thin emerald timeline
- Gold event markers
- Serif event names
- Sans-serif metadata

---

# 18. Festival Values

Present the four core ideas:

```text
01
СИЛА

02
ОПОРА

03
СВОБОДА

04
СПІЛЬНОТА
```

Each item can contain:

- Number
- Large heading
- Short description
- Decorative line or feather element

Use large whitespace.

---

# 19. Location

Recommended layout:

```text
┌──────────────────────┬──────────────────────┐
│                      │                      │
│       PHOTO          │       ЛОКАЦІЯ        │
│                      │                      │
│                      │       Address        │
│                      │                      │
│                      │ ЯК ДІСТАТИСЯ →       │
└──────────────────────┴──────────────────────┘
```

Combine:

- Large image
- Address
- Map
- Directions CTA

---

# 20. Tickets

Ticket section should be visually strong.

Use emerald background:

```text
Будь частиною ЛІМАЛ FEST

[ КУПИТИ КВИТОК ]
```

Visual treatment:

- Emerald background
- White / gold typography
- Feather
- Gold particles
- Gold arc

Keep the CTA extremely clear.

---

# 21. Footer

Minimal and spacious.

```text
LOGO

Про фестиваль
Програма
Учасники
Локація

Instagram
Facebook
Telegram

© ЛІМАЛ FEST
```

Use a subtle gold decorative element near the bottom.

---

# 22. Forms

Create:

- Text Input
- Email Input
- Textarea
- Select
- Checkbox
- Radio
- Search
- Newsletter Form

## Default

```text
Background: transparent
Border-bottom: 1px solid #D8DDD8
```

## Focus

```text
Border-bottom: 2px solid #D5A54A
```

## Error

Use a clear accessible error treatment without introducing unrelated colors unless necessary.

## Success

Use an accessible success state.

Labels should always be visible and not rely only on placeholders.

---

# 23. Iconography

Use minimal line icons.

```text
Stroke: 1.5px
Fill: none
Line caps: round
Line joins: round
Primary color: #123F39
```

Required icon set:

```text
Calendar
Clock
MapPin
Ticket
ArrowRight
ArrowUpRight
Instagram
Facebook
Telegram
Menu
Close
Play
ChevronDown
ChevronRight
Plus
Minus
```

Icons should remain visually secondary to typography.

---

# 24. Images

Photography should feel:

- authentic
- artistic
- emotional
- cinematic
- human
- culturally relevant

Avoid generic stock photography.

### Image treatment

Prefer:

- natural lighting
- documentary moments
- artistic compositions
- muted natural colors
- strong human presence

Avoid excessive filters.

---

# 25. Motion System

Motion should feel slow, elegant and organic.

## Timing

```text
Fast:    200–300ms
Medium:  400–500ms
Slow:    600–700ms
```

## Hero entrance

1. Logo fades in
2. Gold arc draws from left to right
3. Feather subtly moves upward
4. Headline fades/slides upward
5. Gold particles appear gradually

## Hover

```text
Image → scale(1.03)
Arrow → translateX(4px)
Line → expand
Opacity → subtle transition
```

Avoid:

```text
Bounce
Elastic
Aggressive scaling
Fast rotation
Excessive parallax
```

---

# 26. Accessibility

## Contrast

Primary text:

```text
#123F39
```

on:

```text
#F5F8F4
#E8F0E9
```

should remain highly readable.

Do not use light gold as body text.

## Interaction

Minimum touch target:

```text
44 × 44px
```

Provide:

- visible focus states
- keyboard navigation
- semantic HTML
- accessible labels
- descriptive alt text
- reduced-motion support

---

# 27. Responsive Design

## Desktop

Prioritize:

- large typography
- editorial compositions
- photography
- decorative elements
- large whitespace

## Tablet

- Reduce typography
- Preserve editorial layouts
- Move complex grids toward two columns

## Mobile

- One-column layouts
- Smaller decorative elements
- Maintain expressive typography
- Full-width CTAs where appropriate
- Mobile navigation
- Reduced section spacing
- Avoid horizontal overflow

---

# 28. Homepage Architecture

## 01 — Hero

Festival name, dates, tagline and CTA.

## 02 — Про фестиваль

Large editorial statement and photography.

Example:

> Фестиваль, що об'єднує людей, мистецтво та свободу.

## 03 — Програма

Editorial timeline with dates and events.

## 04 — Учасники

Large photography-led artist cards.

## 05 — Ідея фестивалю

Four values:

- СИЛА
- ОПОРА
- СВОБОДА
- СПІЛЬНОТА

## 06 — Локація

Photography + location + map.

## 07 — Квитки

Strong emerald CTA section.

## 08 — Footer

Minimal navigation, social links and branding.

---

# 29. Component Library

The design system should contain reusable components.

## Navigation

- Header
- Mobile Header
- Desktop Navigation
- Mobile Navigation
- Footer
- Breadcrumbs

## Actions

- Primary Button
- Secondary Button
- Text Button
- Icon Button
- Link
- CTA

## Content

- Section Header
- Event Card
- Artist Card
- Ticket Card
- Quote
- Image Gallery
- Program Timeline
- Statistic
- Badge

## Forms

- Input
- Textarea
- Select
- Checkbox
- Radio
- Search
- Newsletter

## Feedback

- Modal
- Toast
- Tooltip
- Alert
- Loading State
- Empty State
- Error State

## Navigation

- Tabs
- Accordion
- Pagination
- Dropdown

## Decorative

- Feather
- Bird
- Gold Arc
- Gold Particles
- Brush Stroke
- Organic Line
- Decorative Divider

---

# 30. Component States

Every interactive component should support:

```text
Default
Hover
Focus
Active
Selected
Disabled
Loading
Error
Success
```

States should remain consistent throughout the website.

---

# 31. Semantic Design Tokens

```css
:root {
  /* Brand */

  --color-brand-primary: #1C5B50;
  --color-brand-dark: #123F39;
  --color-brand-secondary: #3F8174;

  --color-brand-background: #E8F0E9;
  --color-brand-background-soft: #F5F8F4;

  --color-brand-gold: #D5A54A;
  --color-brand-gold-dark: #A87320;
  --color-brand-gold-light: #E8C77D;


  /* Neutral */

  --color-white: #FFFFFF;
  --color-gray-100: #F1F3F0;
  --color-gray-300: #D8DDD8;
  --color-gray-500: #89918B;
  --color-gray-700: #4B544F;
  --color-black: #17201D;


  /* Typography */

  --font-display: "Cormorant Garamond", serif;
  --font-body: "Manrope", sans-serif;


  /* Radius */

  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-pill: 999px;


  /* Spacing */

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;
  --space-9: 96px;
  --space-10: 128px;
  --space-11: 160px;


  /* Layout */

  --container-max-width: 1280px;
  --grid-gap: 24px;


  /* Motion */

  --duration-fast: 250ms;
  --duration-medium: 450ms;
  --duration-slow: 650ms;
}
```

---

# 32. CSS Foundation

```css
* {
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  margin: 0;
  background: #F5F8F4;
  color: #123F39;
  font-family: "Manrope", sans-serif;
  font-size: 17px;
  line-height: 1.55;
}

h1,
h2,
h3,
h4 {
  margin: 0;
  font-family: "Cormorant Garamond", serif;
  font-weight: 500;
}

button,
input,
textarea,
select {
  font: inherit;
}

button {
  cursor: pointer;
}

img {
  display: block;
  max-width: 100%;
}
```

---

# 33. Design Principles

## 01 — Editorial first

Typography and photography should lead the visual experience.

## 02 — Less but better

Every decorative element should have a purpose.

## 03 — Air is part of the design

Use generous whitespace.

## 04 — Gold is precious

Use gold sparingly.

## 05 — Organic + structured

Combine flowing forms from the logo with a clean modern grid.

## 06 — Ukrainian without clichés

The Ukrainian identity should feel contemporary rather than overly ornamental.

## 07 — Premium without being corporate

Use sophisticated typography, spacing and photography instead of excessive effects.

## 08 — Motion should breathe

Animations should feel natural and slow.

---

# 34. Visual Hierarchy

Priority order:

```text
1. Festival identity
2. Main message
3. Photography
4. Primary CTA
5. Section content
6. Metadata
7. Decorative elements
```

Decorative elements should never compete with the primary message.

---

# 35. Final Art Direction

The final website should communicate:

> **Українська культура, свобода, мистецтво та спільнота — через сучасну преміальну візуальну мову.**

The overall feeling should be:

```text
Elegant
        +
Editorial
        +
Ukrainian
        +
Natural
        +
Premium
        +
Modern
```

The logo is the source of the visual language.

The website should feel like the logo has evolved into a complete digital ecosystem rather than simply being placed into a website template.
