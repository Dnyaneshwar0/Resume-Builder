# main.py

from utils.helpers import read_file, save_file, version_control_save
from ocr.ocr_processor import extract_text_from_image
from optimizer.content_optimizer import optimize_content
from parser.resume_parser import parse_resume
from formatter.latex_formatter import format_to_latex
from scorer.ats_scorer import score_resume_against_job
from cover_letter.generator import generate_cover_letter

def main(image_path, job_keywords, industry="general"):
    raw_text = extract_text_from_image(image_path)
    polished_text = optimize_content(raw_text)
    resume_data = parse_resume(polished_text)
    print("Extracted Resume Data:", resume_data)
    print("Raw OCR Text:", raw_text)
    print("🧠 Cleaned Skills for ATS:", resume_data['skills'])

    latex = format_to_latex(resume_data, industry)
    score, matched_keywords = score_resume_against_job(resume_data['skills'], job_keywords)
    print(f"\n🎯 Final ATS Score: {score}%")
    print(f"🔍 Matched Skills: {', '.join(matched_keywords)}")
    print(f"📉 Missing Skills: {', '.join(set([kw.lower() for kw in job_keywords]) - matched_keywords)}\n")

    cover_letter = generate_cover_letter(resume_data["name"], "Software Engineer", "OpenAI", resume_data["skills"])

    save_file(latex, "output/resume.tex")
    version_control_save("resume", polished_text)
    save_file(cover_letter, "output/cover_letter.txt")

    print(f"✅ Resume ATS Score: {score}%")
    print(f"✅ Matched Keywords: {', '.join(matched_keywords)}")

# Uncomment to run
main("media/sample.PNG", ["Python", "AI", "ML", "Leadership"])