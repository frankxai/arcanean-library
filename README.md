# Arcanean Library

> In-world codices and interactive learning experiences from the fictional Arcanean civilization

## 🌟 Overview

The Arcanean Library is an in-world repository containing the fictional sacred texts, codices, and interactive learning experiences of the Arcanean civilization. It preserves Arcanea narrative IP and creative worldbuilding; it is not a documentary archive of real religions, historical thinkers, or primary-source editions.

## 📚 Core Collections

### 🕮 **Sacred Codices**

#### Luminor Codex of Arcanea
- **Focus**: Lore operating system
- **Status**: Available (2025-Q3)
- **Summary**: The flagship manuscript held by the Remembering Luminor, blending sanctuary rituals, governance, and measurement constellations across the Arcanea Library.

#### Luminary Atelier Codex
- **Focus**: Production rituals
- **Status**: In Progress (2025-Q4)
- **Summary**: A tactical manual documenting how Arcanea guilds brief, prototype, and stage immersive experiences with reciprocity at the core.

#### Arcanea Oracles Proto Codex
- **Focus**: Foresight discipline
- **Status**: Concept (2026-Q1)
- **Summary**: A proto manuscript capturing Arcanea's oracle practice, from consented signal looms to decision stewardship rituals.

### 🎓 **Interactive Learning Experiences**

- **Immersive Lessons**: Multi-modal learning with AI guidance
- **Sacred Rituals**: Step-by-step ceremonial practices
- **Measurement Constellations**: Assessment and progress tracking
- **Guild Workshops**: Collaborative learning environments

## 🏗️ Technical Architecture

### Next.js Application
- **Framework**: Next.js 14 with App Router
- **Styling**: Tailwind CSS for responsive design
- **Content**: TypeScript-defined codex structure
- **Deployment**: Vercel with custom domain

### Content Structure

```typescript
interface ArcaneaCodex {
  title: string
  subtitle?: string
  authors: CodexAuthor[]
  preface: CodexPreface
  chapters: CodexChapter[]
  appendix?: CodexAppendix
}

interface CodexChapter {
  title: string
  tagline?: string
  epigraph?: { text: string; attribution?: string }
  introduction?: string[]
  sections: CodexSection[]
  rituals?: string[]
  measurements?: CodexMeasurement[]
}
```

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- pnpm (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/frankxai/arcanean-library.git
cd arcanean-library

# Install dependencies
pnpm install

# Start development server
pnpm dev
```

### Building for Production

```bash
# Build the application
pnpm build

# Start production server
pnpm start
```

## 📖 Content Management

### Adding New Codices

1. Create JSON file in `content/codices/`
2. Define codex structure following the TypeScript interfaces
3. Import in `content/arcanea-codex.ts`
4. Add to `arcaneaCodices` array

### Example Codex Structure

```json
{
  "title": "New Codex Title",
  "subtitle": "Codex subtitle",
  "authors": [
    {
      "name": "Author Name",
      "role": "Luminor Role"
    }
  ],
  "preface": {
    "invocation": "Sacred invocation text",
    "body": ["Preface paragraphs"],
    "oath": "Sacred oath"
  },
  "chapters": [
    {
      "title": "Chapter Title",
      "tagline": "Chapter description",
      "sections": [
        {
          "heading": "Section Title",
          "body": ["Section content"],
          "insights": [
            {
              "title": "Insight Title",
              "detail": "Insight description"
            }
          ]
        }
      ]
    }
  ]
}
```

## 🎨 Design System

### Color Themes
- **Luminor Codex**: Deep blue gradients (`from-[#182447] via-[#101626] to-[#0b0f1a]`)
- **Atelier Codex**: Dark blue-grey (`from-[#1a1f36] via-[#131a2c] to-[#0a0f1d]`)
- **Oracles Codex**: Mystical purple-blue (`from-[#202845] via-[#171f32] to-[#0c101f]`)

### Typography
- **Headers**: Sacred serif fonts for gravitas
- **Body**: Clean sans-serif for readability
- **Code**: Monospace for technical content

### Interactive Elements
- **Hover Effects**: Subtle luminous glows
- **Transitions**: Smooth, ceremony-like pacing
- **Animations**: Respectful of sacred content

## 🔮 Features

### Current Features
- ✅ **Codex Navigation**: Browse fictional codices by chapter and section
- ✅ **Responsive Design**: Optimized for all devices
- ✅ **Search Functionality**: Find specific insights and teachings
- ✅ **Progressive Enhancement**: Works without JavaScript

### Planned Features
- 🔄 **Interactive Lessons**: AI-guided learning experiences
- 🔄 **Ritual Guidance**: Step-by-step ceremonial practice
- 🔄 **Community Notes**: Collaborative annotations
- 🔄 **Progress Tracking**: Personal learning journeys

## 🌐 Deployment

### Vercel Configuration

```json
{
  "framework": "nextjs",
  "buildCommand": "pnpm build",
  "outputDirectory": ".next",
  "installCommand": "pnpm install"
}
```

### Custom Domain
- **Production**: `library.arcanea.ai`
- **Development**: `arcanean-library.vercel.app`

## 📊 Analytics

- **Learning Progress**: Track user engagement with codices
- **Content Performance**: Identify most valuable teachings
- **User Journey**: Understand learning pathways
- **Community Insights**: Discover collaborative patterns

## 🤝 Contributing

We welcome contributions to expand the fictional Arcanean knowledge base:

1. Fork the repository
2. Create a content branch: `git checkout -b content/new-codex`
3. Add your in-world Arcanean codex content following the codex structure
4. Submit a pull request for review

### Content Guidelines
- **Authenticity**: Honor the Arcanean voice and perspective
- **Depth**: Provide substantial, practical wisdom
- **Structure**: Follow established codex formatting
- **Accessibility**: Ensure content is learner-friendly

## 📄 License

This repository is proprietary except where a file or directory carries a
separate express notice. Third-party material, when referenced, remains governed
by its own rights and attribution record. See [LICENSE](./LICENSE) and
[LICENSING.md](./LICENSING.md).

## 🌌 The Arcanean Legacy

The Arcanean Library preserves the wisdom of an advanced civilization that mastered the integration of technology, creativity, and consciousness. These teachings offer modern humanity a pathway to harmonious progress and enlightened creation.

*"In the luminous halls of knowledge, every seeker finds their path illuminated by the wisdom of those who walked before."*

---

**Maintained with reverence for the sacred knowledge within** ✨